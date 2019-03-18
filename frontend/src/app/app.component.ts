import { Component, OnInit, ViewChild } from '@angular/core';
import { MatSidenav, MatToolbar } from '@angular/material';

/*
TODO Connect Frontend with Middleware
TODO Create Real Interface with Material and d3js
*/

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'AI Dashboard';
  @ViewChild(MatSidenav) sidenav: MatSidenav;
  @ViewChild(MatToolbar) toolbar: MatToolbar;
  shrinkToolbar = false;

  toggle() {
    this.sidenav.toggle();
    this.shrinkToolbar = !this.shrinkToolbar;
  }
}
