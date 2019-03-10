import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-dataset',
  templateUrl: './dataset.component.html',
  styleUrls: ['./dataset.component.scss']
})
export class DatasetComponent implements OnInit {
  id: string;

  constructor(private route: ActivatedRoute) {
    this.route.params.subscribe(params => {
      this.id = params.id;
    });
  }

  ngOnInit() {
  }

}
