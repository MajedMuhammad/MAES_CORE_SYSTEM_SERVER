const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const { PythonShell } = require("python-shell");

const port = process.env.PORT || 4001;
const index = require("./routes/index");

const app = express();
app.use(index);

const server = http.createServer(app);

const io = socketIo(server);

let options = {
    mode: 'text',
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: './es',
  };

io.on("connection", (socket) => {
    console.log("New client connected");
    
    let pyshell;

    pyshell = new PythonShell('expertSystem.py', options);
    console.log("Python program in progress...");

    var sockBuf = '';

    pyshell.on('message', function (message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
        sockBuf += message;
        var i;
        var l = 0;
        while ((i = sockBuf.indexOf('\n', l)) !== -1) {
          socket.emit('FromAPI', sockBuf.slice(l, i));
          l = i + 1;
        }
        if (l) {
            sockBuf = sockBuf.slice(l);
        }
    });

    socket.on("FromClient", (res) => {
        console.log(res);
        // sends a message to the Python script via stdin
        if (!pyshell.terminated) {
            pyshell.send(res);
        }
    });
    
    if (pyshell.terminated){
        console.log("Python program is terminated.")
        // end the input stream and allow the process to exit
        pyshell.end(function (err, code, signal) {
            if (err) throw err;
            console.log('The exit code was: ' + code);
            console.log('The exit signal was: ' + signal);
            console.log('finished');
        });
    }

    socket.on("disconnect", () => {
        console.log("Client disconnected");
    }); 
});

server.listen(port, () => console.log(`Listening on port ${port}`));