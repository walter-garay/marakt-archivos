import { Injectable } from '@angular/core';
import { Usuario } from 'src/model/Usuario.model';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ServiceService {
  private ApiUrl = "http://127.0.0.1:8000/api"; // URL to web api
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    })

  };
  constructor(private http: HttpClient) { }


  //USUARIO---
    
  public getUsuarios(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(this.ApiUrl+ 'Usuario/',this.httpOptions)
  }

public postUsuarios(usu:Usuario):Observable<void>{
  let body = JSON.stringify(usu);
  return this.http.post<void>(this.ApiUrl + 'Usuario/',body,this.httpOptions);
  }

public deleteUsuario(id:string): Observable<void> {
  return this.http.delete<void>(this.ApiUrl + 'Usuario/' + id + '/',this.httpOptions)
  }

 public putUsuario(usu:Usuario):Observable<void>{
  let body = JSON.stringify(usu);
  return this.http.put<void>(this.ApiUrl + 'Usuario/' + usu.id + '/',body,this.httpOptions);
  }
}
