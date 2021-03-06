'use strict';

module.exports = function(grunt) {
    grunt.initConfig({

        npmConfig: grunt.file.readJSON('package.json'),
        bowerConfig: grunt.file.readJSON('bower.json'),
		
	    //background watch 	
       bgShell: {
		  _defaults: {
			bg: true
			},
			watchSass: {
				cmd: 'grunt watchSass'
			}
		  }, 
        
        bowercopy: {
            // Bootstrap관련 자바스크립트 파일들을 프로젝트 폴더/js 밑으로 복사
            // Bootstrap관련 폰트 파일들을 프로젝트 폴더/fonts 밑으로 복사
            // Bootstrap관련 Sass 파일들을 프로젝트 폴더/scss 밑으로 복사
            // bootstrap_theme 관련 js, font, sass 파일을 복사
            bootstrap :{
                options: {
                    'srcPrefix': 'bower_components/bootstrap-sass-official/assets'
                },
                files: {
                    'awesomepose/static/js/bootstrap' : 'javascripts',
                    'awesomepose/static/fonts/bootstrap' : 'fonts',
                    'awesomepose/static/scss/bootstrap' : 'stylesheets'
                }
            },
            bootstrap_theme :{
                options: {
                    'srcPrefix': 'bower_components/bootswatch-sass'
                },
                files: {
                    'awesomepose/static/scss/theme' : 'cosmo'
                }
            },
            // jQuery를 프로젝트 폴더/js 밑으로 복사
            jquery : {
                options: {
                    'srcPrefix': 'bower_components'
                },
                files: {
                    'awesomepose/static/js/jquery': 'jquery/dist',
                }
            },
            bootstrap_social:{
                options: {
                    'srcPrefix': 'bower_components/bootstrap-social'
                },
                files: {
                    'awesomepose/static/scss/social' : 'bootstrap-social.scss',
                }
            },
            font_awesome:{
                options: {
                    'srcPrefix': 'bower_components/font-awesome'
                },
                files: {
                    'awesomepose/static/fonts' : 'fonts',
                    'awesomepose/static/scss/font-awesome' : 'scss',
                }
            },
        },
        // compass 파일을 컴파일
        compass: {
            dist: {
                options: {
                    sassDir: 'scss',
                    cssDir: 'css'
                }
            }
        },

        // Sass 파일을 컴파일
        sass: {
          dist: {
            options: {
              style: 'expanded', // 이전
              //style: 'compressed', // 압축 옵션 설정
              precision: 8
            },
            files: [{
               'awesomepose/static/css/application.css': 'awesomepose/static/scss/application.scss'
              //'css/application.min.css': 'scss/application.scss' // minified 버전
            }]
          }
        },

        watch:{
                files:'awesomepose/static/scss/application.scss',
                tasks:['sass'],
    			options: {
                		spawn: false
            			},
        } 

    })

    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-bowercopy');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-bg-shell');

    grunt.registerTask('run-sass', ['bowercopy', 'sass']);
    grunt.registerTask('watchSass', ['watch']); 
    grunt.registerTask('default', ['bgShell:watchSass']);

}
