import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Testset } from '../testset';
import { AiService } from '../ai.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: [ './dashboard.component.scss' ]
})
export class DashboardComponent implements OnInit {
  testset: Testset[] = [];
  module = 'Dashboard';

  constructor(
    private http: HttpClient,
    private aiService: AiService) { }

  ngOnInit() {
    this.getHeroes();
  }

  getHeroes(): void {
    this.aiService.getTestset()
      .subscribe(testset => this.testset = testset.slice(0, 4));
  }
}
