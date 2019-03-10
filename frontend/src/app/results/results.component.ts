import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator, MatSort, MatInput } from '@angular/material';
import { merge, Observable, of as observableOf, fromEvent } from 'rxjs';
import { debounceTime, distinctUntilChanged, tap, delay } from 'rxjs/operators';
import { catchError, map, startWith, switchMap } from 'rxjs/operators';

/**
 * @title Table retrieving data through HTTP
 */
@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss'],
})
export class ResultsComponent implements OnInit {
  displayedColumns: string[] = ['name', 'created_at', 'select'];
  exampleDatabase: Datasource | null;
  data: any[] = [];

  resultsLength = 0;
  isLoadingResults = true;
  isRateLimitReached = false;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;
  @ViewChild('input') input: ElementRef;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.exampleDatabase = new Datasource(this.http);

    this.sort.sortChange.subscribe(() => this.paginator.pageIndex = 0);

    fromEvent(this.input.nativeElement, 'keyup')
      .pipe(
        debounceTime(150),
        distinctUntilChanged(),
        startWith({}),
        switchMap(() => {
          this.isLoadingResults = true;
          return this.exampleDatabase!.getData(
            this.sort.active, this.sort.direction, this.paginator.pageIndex, this.input.nativeElement.value,);
        }),
        map(data => {
          // Flip flag to show that loading has finished.
          this.isLoadingResults = false;
          this.isRateLimitReached = false;
          console.log(data)
          this.resultsLength = data.recordsTotal;
          return data.data;
        }),
        catchError(() => {
          this.isLoadingResults = false;
          console.log("bla")
          // Catch if the GitHub API has reached its rate limit. Return empty data.
          this.isRateLimitReached = true;
          return observableOf([]);
        })
      ).subscribe(data => this.data = data);

    merge(this.sort.sortChange, this.paginator.page)
      .pipe(
        startWith({}),
        switchMap(() => {
          this.isLoadingResults = true;
          return this.exampleDatabase!.getData(
            this.sort.active, this.sort.direction, this.paginator.pageIndex, this.input.nativeElement.value,);
        }),
        map(data => {
          // Flip flag to show that loading has finished.
          this.isLoadingResults = false;
          this.isRateLimitReached = false;
          console.log(data)
          this.resultsLength = data.recordsTotal;
          return data.data;
        }),
        catchError(() => {
          this.isLoadingResults = false;
          console.log("bla")
          // Catch if the GitHub API has reached its rate limit. Return empty data.
          this.isRateLimitReached = true;
          return observableOf([]);
        })
      ).subscribe(data => this.data = data);
  }

  applyFilter(searchterm) {
    console.log(searchterm);
  }
}

export interface GithubApi {
  items: any[];
}

export interface GithubIssue {
  dataset_name: string;
  number_of_records: string;
}

/** An example database that the data source uses to retrieve data for the table. */
export class Datasource {
  constructor(private http: HttpClient) { }

  getData(sort: string, order: string, page: number, filter: string): Observable<any> {
    const href = '/api/apis/';
    const requestUrl =
      `${href}?q=repo:angular/material2&sort=${sort}&order=${order}&page=${page}&limit=10&filter=${filter}`;

    return this.http.get<GithubApi>(requestUrl);
  }
}
