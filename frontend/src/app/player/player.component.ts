import { Component, OnInit, Input } from '@angular/core';
import { Quiz } from '../app.type'

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent implements OnInit {

  @Input() index: number;
  @Input() player: string;
  @Input() quiz: Quiz;
  @Input() date: string;

  constructor() { }

  ngOnInit() {
  }

}
