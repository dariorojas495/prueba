import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StainCalculatorComponent } from './stain-calculator.component';

describe('StainCalculatorComponent', () => {
  let component: StainCalculatorComponent;
  let fixture: ComponentFixture<StainCalculatorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StainCalculatorComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StainCalculatorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
