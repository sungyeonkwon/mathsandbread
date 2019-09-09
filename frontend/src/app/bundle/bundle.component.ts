import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Bundle, Quiz } from '../app.type';

@Component({
  selector: 'app-bundle',
  templateUrl: './bundle.component.html',
  styleUrls: ['./bundle.component.scss'],
})
export class BundleComponent implements OnInit {

  bundles: Bundle[];

  constructor(private api: ApiService) {
    this.getAllData();
  }

  getAllData = () => {
    this.api.getAllData().subscribe(
      data => {
        this.bundles = data;
        console.log("this.bundles", this.bundles)
      }, 
      error => {
        console.log(error)
      }
    )
  }

  ngOnInit() {
  }

}