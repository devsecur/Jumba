import { Component, OnInit, ViewChild, ElementRef, Directive, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { MatPaginator, MatSort, MatInput } from '@angular/material';
import { merge, Observable, of as observableOf, fromEvent } from 'rxjs';
import { debounceTime, distinctUntilChanged, tap, delay } from 'rxjs/operators';
import { map, startWith, switchMap } from 'rxjs/operators';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-dataset',
  templateUrl: './dataset.component.html',
  styleUrls: ['./dataset.component.scss']
})
export class DatasetComponent implements OnInit {
  @ViewChild('features') features;
  @ViewChild('questions') questions;

  id: string;
  datasource: Datasource | null;
  api: any;

  constructor(private route: ActivatedRoute, private http: HttpClient) {
    this.route.params.subscribe(params => {
      this.id = params.id;
    });
  }

  ngOnInit() {
    this.datasource = new Datasource(this.http);
    this.datasource
      .getData(`/api/apis/${this.id}`)
      .pipe(
        map(data => {
          console.log(data);
          return data.api;}
        )
      ).subscribe(data => {
        this.api = data;
        this.features.getFeatures(this.api, this.datasource)
      }
      );
  }
}

export class Datasource {
  constructor(private http: HttpClient) { }

  getData(endpoint: string): Observable<any> {
    return this.http.get<any>(`${endpoint}`);
  }
}

@Directive({ selector: '[indeterminate]' })
export class IndeterminateDirective {
   @Input()
   set indeterminate(value)
   {
     this.elem.nativeElement.indeterminate=value;
   }
    constructor(private elem: ElementRef) {
    }
}
