import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common'; // ✅ Usar CommonModule en vez de BrowserModule
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-stain-calculator',
  standalone: true,
  templateUrl: './stain-calculator.component.html',
  styleUrl: './stain-calculator.component.css',
  imports: [
    CommonModule, // ✅ Reemplaza BrowserModule con CommonModule
    FormsModule
  ]
})
export class StainCalculatorComponent {
  @Input() imageData: ImageData | null = null;
  @Output() areaCalculated = new EventEmitter<number>();
  numPoints = 1000;

  calculateArea() {
    if (!this.imageData) return;
    let insideCount = 0;
    const { width, height, data } = this.imageData;

    for (let i = 0; i < this.numPoints; i++) {
      const x = Math.floor(Math.random() * width);
      const y = Math.floor(Math.random() * height);
      const index = (y * width + x) * 4;
      if (data[index] === 255) insideCount++;
    }

    const totalArea = width * height;
    const estimatedArea = (insideCount / this.numPoints) * totalArea;
    this.areaCalculated.emit(estimatedArea);
  }
}
