#!/usr/bin/env node

var Child_Proc = require('child_process');
var AppForm = Child_Proc.spawn('python3', ['app_win.py']);

AppForm.stdout.on('data', (recv) =>
{
    console.log(recv.toString().trim());
});

setTimeout(() =>
{
    AppForm.stdin.write("6 second notice\n");

},  6000  );
