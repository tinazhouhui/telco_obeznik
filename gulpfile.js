/* eslint-disable no-console */

const gulp = require('gulp');
const gulpSass = require('gulp-sass');
const sassVars = require('gulp-sass-vars');
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const rename = require('gulp-rename');
const yargs = require('yargs');

const appVersion = (typeof (yargs.argv.appVersion) !== 'undefined') ? yargs.argv.appVersion : 'dev';
const publicUrl = (typeof (yargs.argv.publicUrl) !== 'undefined') ? yargs.argv.publicUrl : '/test/..';

const sass = () => {
  return gulp.src('scss/style-*.scss')
    .pipe(sassVars({
      appVersion: appVersion,
      publicUrl: publicUrl,
    }, {verbose: true}))
    .pipe(gulpSass())
    .pipe(gulp.dest('www/css'));
};

const cssmin = () => {
  return gulp.src(['www/css/*.css', '!www/css/*.min.css'])
    .pipe(postcss([
      autoprefixer(),
      cssnano({
        reduceIdents: false
      })
    ]))
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('www/css'));
};

const css = gulp.series(sass, cssmin);

const watch = (callback) => {
  gulp.watch(['scss/**/*.scss'], css);

  return gulp.series(callback);
};

const production = css;

const defaultTask = gulp.series(production, gulp.parallel(watch));

exports.default = defaultTask;
exports.production = production;
