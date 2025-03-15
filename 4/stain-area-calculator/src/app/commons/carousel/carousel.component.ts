import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatStepperModule } from '@angular/material/stepper';
import { MatButtonModule } from '@angular/material/button';
import { UploadImageComponent } from '../../components/upload-image/upload-image.component';
import { StainCalculatorComponent } from '../../components/stain-calculator/stain-calculator.component';
import { ResultsTableComponent } from '../../components/results-table/results-table.component';
import { StainService } from '../../services/stain.service';

@Component({
  selector: 'app-carousel',
  standalone: true,
  imports: [
    CommonModule,
    MatStepperModule,
    MatButtonModule,
    UploadImageComponent,
    StainCalculatorComponent,
    ResultsTableComponent
  ],
  templateUrl: './carousel.component.html',
  styleUrl: './carousel.component.css'
})
export class CarouselComponent {
  imageData: ImageData | null = null;
  calculatedArea: number | null = null;
  results: { area: number, timestamp: Date }[] = [];

  constructor(private stainService: StainService) {}

  onImageUploaded(imageData: ImageData) {
    this.imageData = imageData;
  }

  onAreaCalculated(area: number) {
    this.calculatedArea = area;
    this.results.push({ area, timestamp: new Date() });
    this.stainService.saveResult(area);
  }
}
