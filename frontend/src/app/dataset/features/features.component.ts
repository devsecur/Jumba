import { Component, OnInit, ViewChild, ElementRef, Directive, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { MatPaginator, MatSort, MatInput } from '@angular/material';
import { merge, Observable, of as observableOf, fromEvent } from 'rxjs';
import { debounceTime, distinctUntilChanged, tap, delay } from 'rxjs/operators';
import { map, startWith, switchMap } from 'rxjs/operators';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-features',
  templateUrl: './features.component.html',
  styleUrls: ['./features.component.scss']
})
export class FeaturesComponent implements OnInit {
  data: any[] = [];
  client:any={indeterminated:true}
  tape = [null, true, false];

  done = null;

  doneControl = new FormControl(false);

  constructor() { }

  ngOnInit() {
  }

  getFeatures(api: any, datasource: any) {
    let url = api.url_matches[0].frontend_prefix
    datasource
      .getData(`${url}/format`)
      .pipe(
        map(result => {
          console.log(result);
          return result;
        })
      ).subscribe(result => {
        this.data = result;})
  }

  click(item: any) {
    item.done = this.tape[(this.tape.indexOf(item.done) + 1) % this.tape.length]
    console.log(item)
  }


}
