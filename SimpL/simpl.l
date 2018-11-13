%{
#include <stdlib.h>
#include "y.tab.h"
void yyerror(char *);
%}
%option yylineno
%x STR
%%

"=="            return EQ;
"!="            return NE;
">="            return GE;
"<="            return LE;
"newline"       return NEWLINE;
"comment"		return COMMENT;
"if"            return IF;
"while"         return WHILE;
"do"            return DO;
"then"          return THEN;
"else"          return ELSE;
"endif"         return ENDIF;
"print"         return PRINT;


[a-zA-Z]+ { yylval = *yytext - 'a'; return VARIABLE;}

[0-9]+ {  yylval = atoi(yytext); return INTEGER; }

[><=+*;\(\).-] { return *yytext; }

<INITIAL>\"                 { BEGIN(STR); }
<STR>[^"]*\"                { 
                                BEGIN(INITIAL);
                                yylval=strndup(yytext, strlen(yytext) - 1);
                                return STRING;
                            }

\/\/.* ;                // Ignore comments

[ \t\n]+        ;       // ignore whitespace

.               yyerror("Unknown character");
%%
int yywrap(void) {
    return 1;
}
