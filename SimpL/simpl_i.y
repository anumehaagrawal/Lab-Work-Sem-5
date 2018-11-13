%{
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>

int yylex(void);
void yyerror(char *s);
int sym[26];                    /* symbol table */
%}



%token INTEGER
%token VARIABLE
%token STRING
%token IF RETURN PRINT PRINTSTR PRINTNL THEN ENDIF ELSE NEWLINE COMMENT WHILE DO

%nonassoc IFX
%nonassoc ELSE
%left GE LE EQ NE '>' '<'
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS
%nonassoc UPLUS


%%

prog:
        stmt_list           
        ;

stmt_list:
        stmt_list stmt      
        | stmt              
        ;

stmt:
        assign_stmt         
        | print_stmt        
        | if_stmt  
        | while_stmt        
        ;

assign_stmt:
        VARIABLE{push();} '='{push();} expr{codegen_assign();} ';'{push();}   
        ;

print_stmt:
        PRINT{push();} expr{codegen_assign();} ';'{push();}            
        | PRINT{push();} STRING{val();} ';'{push();}         
        | PRINT{push();}  NEWLINE{val();}  ';'{push();}         
    
        ;

if_stmt:
               
        IF expr rule1 THEN stmt_list rule2 ELSE stmt_list ENDIF rule3 
        | IF expr rule1 THEN stmt_list ENDIF rule2  
        
        ;
while_stmt :
        WHILE rule4 '(' expr ')' rule5 expr ';'rule6


        ;

rule1 : {lab3();}
        ;
rule2 : {lab4();}
        ;
rule3 : {lab5();}
        ;
rule4 : {lab6();}
        ;
rule5 : {lab7();}
        ;
rule6 : {lab8();}
        ;

expr:
        INTEGER {push();}                 
        | VARIABLE  {push();}           
	    | '+'{push();} expr{codegen_umax();} %prec UPLUS  
        | '-'{push();} expr{codegen_umin();} %prec UMINUS 
        | expr '*'{push();} expr{codegen();}       
        | expr '/'{push();} expr{codegen();}       
        | expr '+'{push();} expr{codegen();}       
        | expr '-'{push();} expr{codegen();}       
        | expr '<'{push();} expr{codegen();}       
        | expr '>'{push();} expr{codegen();}       
        | expr EQ {push();} expr{codegen();}          
        | expr GE {push();} expr{codegen();} 
        | expr '=' {push();} expr{codegen();}          
        | expr NE {push();} expr{codegen();}          
        | expr LE {push();} expr{codegen();}           
        | '(' expr ')'          
        ;

%%

#include "lex.yy.c"
#include<ctype.h>
char st[100][10];
int top=0;
char i_[2]="0";
char temp[2]="t";
int start =1 ;
int label[20];
int lnum=1;
int ltop=0;



void yyerror(char *s) {
    extern yylineno;
    fprintf(stdout, "%s\nLine No: %d\n", s, yylineno);
}

int main(void) {
    printf("Enter expression");
    yyparse();
    return 0;
}

push()
 {
  strcpy(st[++top],yytext);
 }
val(){
     printf("%s\n",st[top]);
     top-=2;
}
 codegen()
 {
 strcpy(temp,"t");
 strcat(temp,i_);
  printf("%s = %s %s %s\n",temp,st[top-2],st[top-1],st[top]);
  top-=2;
 strcpy(st[top],temp);
 i_[0]++;
 }

codegen_umin()
 {
 strcpy(temp,"t");
 strcat(temp,i_);
 printf("%s = -%s\n",temp,st[top]);
 top--;
 strcpy(st[top],temp);
 i_[0]++;
}

codegen_umax()
 {
 strcpy(temp,"t");
 strcat(temp,i_);
 printf("%s = +%s\n",temp,st[top]);
 top--;
 strcpy(st[top],temp);
 i_[0]++;
 }

codegen_assign()
 {
 printf("%s = %s\n",st[top-2],st[top]);
 top-=2;
}

lab1()
{
 lnum++;
 strcpy(temp,"t");
 strcat(temp,i_);
 printf("%s = not %s\n",temp,st[top]);
 printf("if %s goto L%d\n",temp,lnum);
 i_[0]++;
 label[++ltop]=lnum;
}

lab2()
{
int x;
lnum++;
x=label[ltop--];
printf("goto L%d\n",lnum);
printf("L%d: \n",x);
label[++ltop]=lnum;
}

lab3()
{
 lnum++;
 strcpy(temp,"t");
 strcat(temp,i_);
 printf("%s = not %s\n",temp,st[top]);
 printf("if %s goto L%d\n",temp,lnum);
 i_[0]++;
 label[++ltop]=lnum;
}

lab4()
{
int x;
lnum++;
x=label[ltop--];
printf("goto L%d\n",lnum);
printf("L%d: \n",x);
label[++ltop]=lnum;
}

lab5()
{
int y;
y=label[ltop--];
printf("L%d: \n",y);
}

