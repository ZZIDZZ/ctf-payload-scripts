excerpt from https://blog.p6.is/AST-Injection/

AST injection, or prototype pollution caused by a module "pug", and other select few modules

If prototype pollution vulnerability exists in the JS application,
Any AST can be inserted in the function by making it insert during the Parser or Compiler process.

Here, you can insert AST without proper filtering of input (which has not been properly filtered) that has not been verified by lexer or parser.
Then, we can give unexpected input to the compiler.
