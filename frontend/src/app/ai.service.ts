import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { Testset } from './testset';
import { TESTSET } from './mock-testset';
import { MessageService } from './message.service';

@Injectable({ providedIn: 'root' })
export class AiService {

  constructor(private messageService: MessageService) { }

  getTestset(): Observable<Testset[]> {
    this.messageService.add('HeroService: fetched heroes');
    return of(TESTSET);
  }

  getTest(id: number): Observable<Testset> {
    this.messageService.add(`HeroService: fetched hero id=${id}`);
    return of(TESTSET.find(hero => hero.id === id));
  }
}
