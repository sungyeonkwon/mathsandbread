import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'front-mathsandbread';

  constructor(private api: ApiService) {
    this.getAllData();
  }

  getAllData = () => {
    this.api.getAllData().subscribe(
      data => {
        console.log("data", data)
      }, 
      error => {
        console.log(error)
      }
    )
  }
}
