import { Component } from '@angular/core';
import { UploadImageComponent } from '../../components/upload-image/upload-image.component';
import { StainCalculatorComponent } from '../../components/stain-calculator/stain-calculator.component';
import { ResultsTableComponent } from '../../components/results-table/results-table.component';
import { CarouselComponent } from '../../commons/carousel/carousel.component';
import { StainService } from '../../services/stain.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CarouselComponent, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  imageData: ImageData | null = null;
  results: any[] = [];

  constructor(private stainService: StainService) {
    this.stainService.results$.subscribe(res => (this.results = res));
  }

  onImageUploaded(imageData: ImageData) {
    this.imageData = imageData;
  }


}
