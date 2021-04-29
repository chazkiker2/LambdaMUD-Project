const path = require('path');

const plugins = [];

module.exports = {
    entry: "./assets/index.js",  // path to our input file
    output: {
        filename: "bundle.js",  // output bundle file name
        // path: path.resolve(__dirname, "./static"),  // path to our Django static directory
        path: path.resolve(__dirname, "static")
    },
    plugins,
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: {presets: ["@babel/preset-env", "@babel/preset-react"]}
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
}
;
