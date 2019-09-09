import { Component, OnInit, Input } from '@angular/core';
import { Quiz } from '../app.type';

@Component({
  selector: 'app-quizset',
  templateUrl: './quizset.component.html',
  styleUrls: ['./quizset.component.scss']
})
export class QuizsetComponent implements OnInit {
  @Input() quiz: Quiz;
  @Input() date: string;

  constructor() { }

  ngOnInit() {
  }

}
