const path              = require("path");
const mode              = process.env.NODE_ENV;

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

let webpack_config = {
    mode    : mode,
    watch   : mode === "development",
    module  : {
        rules   : [
            {
                test    : /\.js$/,
                exclude : /node_modules/,
                use     : {
                    loader  : "babel-loader",
                    options : {
                        presets : ["@babel/preset-env"]
                    },
                },
            },
            {
                test    : /\.scss$/,
                use     : [
                    {
                        loader  : MiniCssExtractPlugin.loader,
                        options : {
                            publicPath: '/static/dist',
                        }
                    },
                    "css-loader",
                    "sass-loader"
                ],
            },
            {
                test    : /\.css$/,
                use     : [
                    {
                        loader  : MiniCssExtractPlugin.loader,
                        options : {
                            publicPath: '/static/dist',
                        }
                    },
                    "css-loader",
                ],
            },
            {
                test    : /\.(woff2?|ttf|svg|otf|eot)$/,
                exclude : /node_modules/,
                loader: 'file-loader',
                options: {
                    name: 'fonts/[name].[ext]',
                },
            },
            {
                test    : /\.(png|jpg)$/,
                loader: 'file-loader',
                options: {
                    name: 'images/[name].[ext]',
                },
            },
        ],
    },
    plugins : [
        new MiniCssExtractPlugin({
            filename: "[name].css"
        })
    ],
    resolve : {
        alias : {
            vue : 'vue/dist/vue.js'
        },
    },
}

if (mode === "production") {
    // webpack_config.plugins.push()
}

let core = Object.assign({}, webpack_config, {
    entry   : {
        index   : path.resolve("./theme/assets/js/index.js"),
    },
    output  : {
        path            : path.resolve("./static/dist/"),
        filename        : "[name].js",
        sourceMapFilename : "[name][ext].map",
        libraryTarget   : "umd",
    },
    devtool: "source-map"
})

let page_vuejs = Object.assign({}, webpack_config, {
    entry   : {
        home   : path.resolve(
            "./theme/assets/js/pages/home.js"
        ),
    },
    output  : {
        path        : path.resolve("./static/dist/pages/"),
        sourceMapFilename : "[name][ext].map",
        filename    : "[name].js"
    },
    devtool: "source-map"
})

module.exports =[
    core,
    page_vuejs,
];
