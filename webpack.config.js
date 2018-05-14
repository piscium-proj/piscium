const path = require('path');
const HtmlWebPackPlugin = require("html-webpack-plugin");
const htmlPlugin = new HtmlWebPackPlugin({
  template: "./static/html/script-off.html",
  filename: "../html/script-on.html"
});

module.exports = {
  entry: "./static/scripts/app.jsx",
  output: {
    path: path.resolve(__dirname, "static/scripts"),
    filename: "main.js"
  },
  resolve: {
    alias: {
      scripts: path.resolve(__dirname, "static/scripts")
    }
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        use: [
          "style-loader",
          "css-loader"
        ]
      },
      {
        test: /\.scss$/,
        use: [
          "style-loader",
          "css-loader"
        ]
      }
    ]
  },
  plugins: [htmlPlugin]
};