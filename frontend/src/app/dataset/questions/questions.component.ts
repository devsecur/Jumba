import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSelectionList, MatListOption } from '@angular/material';
import {SelectionModel} from '@angular/cdk/collections';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.scss']
})
export class QuestionsComponent implements OnInit {
  @ViewChild(MatSelectionList) selectionList: any;
  question: string;
  newQuestion: string;
  selectedQuestion: any;
  questions: any[] = [ 'What is the question?' ];

  constructor() { }

  ngOnInit() {
  }

  onSelection(options: any) {
    // map these MatListOptions to their values
  }

  addQuestion() {
    this.questions.push(this.newQuestion);
    this.selectedQuestion = this.newQuestion;
  }

}
