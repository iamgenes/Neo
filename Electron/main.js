/* 
This code may now work at the moment its the main file for 
the electron app,
will add the rest of the components soon
*/

const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

const path = require('path');
const url = require('url');
const isDev = require('electron-is-dev');

let mainWindow;

function createWindow() {
  //creating the main window
  mainWindow = new BrowserWindow({ 
    width: 900, 
    height: 680,
    icon: '', 
    title: 'Neo smart assistant',
    frame: true
  });
  mainWindow.loadURL(isDev ? 'http://localhost:3000' : `file://${path.join(__dirname, '../build/index.html')}`);
  mainWindow.on('closed', () => mainWindow = null);
}

//creating the main window after the app is ready
app.on('ready', createWindow);

//closing the window in linux and windows platforms
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

//activating the app from the tastbar.
app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});