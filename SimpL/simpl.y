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
%token IF RETURN PRINT PRINTSTR PRINTNL THEN ENDIF ELSE NEWLINE COMMENT

%nonassoc IFX
%nonassoc ELSE
%left GE LE EQ NE '>' '<'
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS
%nonassoc UPLUS


%%

prog:
        stmt_list           { printf("stmt_list \n"); }
        ;

stmt_list:
        stmt_list stmt      { printf("stmt_list stmt \n"); }
        | stmt              { printf("stmt \n");}
        ;

stmt:
        assign_stmt         { printf("assign_stmt \n"); }
        | print_stmt        { printf("print_stmt \n"); }
        | if_stmt           { printf("if_stmt \n");}
        ;

assign_stmt:
        VARIABLE '=' expr ';'   { printf("VARIABLE = expr ; \n"); }
        ;

print_stmt:
        PRINT expr ';'              { printf(" PRINT expr ;  \n"); }
        | PRINT STRING ';'          { printf("PRINT STRING ; \n"); }
        | PRINT NEWLINE ';'         { printf(" PRINT NEWLINE ; \n"); }
       
        ;

if_stmt:
        IF expr THEN stmt_list ENDIF         { printf(" IF expr THEN stmt_list ENDIF \n"); }
        |IF expr THEN stmt_list ELSE stmt_list ENDIF    { printf(" IF expr THEN stmt_list ELSE stmt_list ENDIF \n"); }
        ;

expr:
        INTEGER                 {  printf("INTEGER \n"); }
        | VARIABLE              { printf(" VARIABLE \n");}
	| '+' expr %prec UPLUS  {  printf(" '+' expr %prec UPLUS\n"); }
        | '-' expr %prec UMINUS {  printf(" '-' expr %prec UMINUS\n"); }
        | expr '*' expr         {  printf(" expr '*' expr  \n"); }
        | expr '/' expr         {  printf("expr '/' expr \n"); }
        | expr '+' expr         { printf(" expr '+' expr \n"); }
        | expr '-' expr         {  printf(" expr '-' expr \n"); }
        | expr '<' expr         { printf(" expr '<' expr \n"); }
        | expr '>' expr         {  printf("expr '>' expr \n"); }
        | expr EQ expr          {  printf(" expr EQ expr  \n"); }
        | expr GE expr          {  printf(" expr GE expr   \n"); }
        | expr NE expr          {  printf(" expr NE expr \n"); }
        | expr LE expr          {  printf(" expr LE expr  \n"); }
        | '(' expr ')'          {  printf(" (  expr ) \n" ); }
        ;

%%


void yyerror(char *s) {
    extern yylineno;
    fprintf(stdout, "%s\nLine No: %d\n", s, yylineno);
}

int main(void) {
    yyparse();
    return 0;
}
