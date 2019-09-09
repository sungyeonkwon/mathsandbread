import { Component, OnInit, Input } from '@angular/core';
import { Bundle, Quiz } from '../app.type';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  @Input() quiz: Quiz;
  @Input() bundles: Bundle[]; 
  @Input() player: string;

  units: Array<any> = Array.from({length: 40}, () => 'default')

  constructor() { 
  }

  ngOnInit() {
    this.updateMap()
  }

  updateMap() {
    const propName = `quiz_for_${this.player}`;
    const statusArr = this.bundles
      .map( v => v[propName].status.toLowerCase());
    this.units.splice(0, statusArr.length);
    this.units.unshift(...statusArr);
  }
}
