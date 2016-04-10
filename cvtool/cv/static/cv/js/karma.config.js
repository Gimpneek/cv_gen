module.exports = function(config) {
    config.set({

        browsers: ['PhantomJS'],

        files: [
            { pattern: 'test-context.js'}
        ],

        frameworks: ['jasmine'],

        preprocessors: {
            'test-context.js': ['webpack']
        },

        webpack: {
            module: {
                loaders: [
                    {
                        test: /\.js/,
                        exclude: /node_modules/,
                        loader: 'babel-loader',
                        query: {
                          presets: ['es2015', 'stage-0']
                        }
                    }
                ]
            },
            watch: true
        }
    });
};