import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StainService } from '../../services/stain.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-results-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './results-table.component.html',
  styleUrl: './results-table.component.css'
})
export class ResultsTableComponent {
  @Input() results: { area: number, timestamp: Date }[] = [];
}
