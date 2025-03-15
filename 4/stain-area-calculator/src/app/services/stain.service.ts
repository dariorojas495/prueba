import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StainService {
  private resultsSubject = new BehaviorSubject<{ area: number, timestamp: Date }[]>([]);
  results$ = this.resultsSubject.asObservable();

  saveResult(area: number) {
    const currentResults = this.resultsSubject.value;
    this.resultsSubject.next([...currentResults, { area, timestamp: new Date() }]);
  }
}
