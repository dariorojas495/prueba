import os
import logging
import pandas as pd
import pydicom
import numpy as np
from typing import Optional, List, Tuple
from datetime import datetime
from PIL import Image

class FileProcessor:
    def __init__(self):
        self.base_path = os.getcwd()
        log_path = self.base_path
        
        log_file = os.path.join(log_path, "logfile.log")
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def analyze_folder(self) -> None:
        for root, dirs, files in os.walk(self.base_path):
            output = f"Folder: {root}\nNumber of elements: {len(dirs) + len(files)}"
            file_info = []
            folder_info = []
            
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                folder_info.append(f" - {folder} (Last Modified: {datetime.fromtimestamp(os.path.getmtime(folder_path))})")
            
            for file in files:
                file_path = os.path.join(root, file)
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                file_info.append(f" - {file} ({size_mb:.2f} MB, Last Modified: {datetime.fromtimestamp(os.path.getmtime(file_path))})")
                
                if file.endswith(".csv"):
                    self.read_csv(file_path)
                elif file.endswith(".dcm"):
                    self.read_dicom(file_path, extract_image=True)
            
            output += f"\nFiles:\n" + "\n".join(file_info) + "\nFolders:\n" + "\n".join(folder_info)
            print(output)
            self.logger.info(output)
    
    def read_csv(self, file_path: str) -> None:
        try:
            df = pd.read_csv(file_path)
            output = f"CSV Analysis:\nColumns: {list(df.columns)}\nRows: {len(df)}"
            
            numeric_cols = df.select_dtypes(include=[np.number])
            if not numeric_cols.empty:
                stats = numeric_cols.describe().loc[['mean', 'std']]
                for col in stats.columns:
                    output += f"\n - {col}: Average = {stats[col]['mean']:.2f}, Std Dev = {stats[col]['std']:.2f}"
            
            non_numeric_cols = df.select_dtypes(exclude=[np.number])
            for col in non_numeric_cols:
                output += f"\n - {col}: Unique Values = {df[col].nunique()}"
            
            print(output)
            self.logger.info(output)
        except Exception as e:
            self.logger.error(f"Error processing CSV file {file_path}: {e}")
            print(f"Error processing the CSV file {file_path}.")

    def read_dicom(self, file_path: str, extract_image: bool = False) -> None:
        try:
            dcm = pydicom.dcmread(file_path)
            output = f"DICOM Analysis:\nPatient Name: {dcm.PatientName}\nStudy Date: {dcm.StudyDate}\nModality: {dcm.Modality}"
            
            tags = [(0x0010, 0x0010), (0x0008, 0x0060)]
            for tag in tags:
                try:
                    output += f"\nTag {hex(tag[0])}, {hex(tag[1])}: {dcm[tag].value}"
                except KeyError:
                    output += f"\nTag {hex(tag[0])}, {hex(tag[1])} not found."
            
            if extract_image and hasattr(dcm, 'PixelData'):
                image_array = dcm.pixel_array
                if len(image_array.shape) > 2 and image_array.shape[2] > 1:
                    image_array = image_array[:, :, 0]  # Tomar solo un canal si es multicanal
                
                image_array = ((image_array - image_array.min()) / (image_array.max() - image_array.min()) * 255).astype(np.uint8)  # Normalizar a 8 bits
                image = Image.fromarray(image_array)
                image_path = file_path.replace('.dcm', '.png')
                image.save(image_path)
                output += f"\nExtracted image saved to {image_path}"
            
            print(output)
            self.logger.info(output)
        except Exception as e:
            self.logger.error(f"Error reading DICOM file {file_path}: {e}")
            print(f"Error reading the DICOM file {file_path}.")

if __name__ == "__main__":
    processor = FileProcessor()
    processor.analyze_folder()
