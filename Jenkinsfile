pipeline {
	agent any
	triggers {
		pollSCM('H/2 * * * *')
	}
	options {
		buildDiscarder(logRotator(numToKeepStr: '7'))
		skipDefaultCheckout()
	}
	stages {
		stage('init') {
			steps {
				echo "Using workspace [${WORKSPACE}]"
				echo "Branch = ${env.BRANCH_NAME}"
				cleanWs()

				checkout([$class: 'GitSCM',
                    branches: [[name: '*/mysql_exp']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'CleanCheckout']],
                    submoduleCfg: [],
                    userRemoteConfigs: [[credentialsId: 'alunwcom-mu', url: 'git@github.com:alunwcom/moanypy.git']]
                ])


// 				checkout scm
// 				sh '''
// 				    git clean -fdx
// 				    git checkout ${BRANCH_NAME}
// 				    git pull --ff-only
//
// 				    VERSION=$(git describe --dirty --always)
// 				    echo "VERSION=${VERSION}"
// 				'''
			}
		}
		stage('build') {
			steps {
// 				echo "Git commit = ${GIT_COMMIT}"
				sh '''
					docker build -t alunwcom/moanypy:latest -f Dockerfile .
				'''
// 				echo "Version = ${env.VERSION}"
			}
		}
		stage('publish') {
			steps {
				echo "TODO"
			}
		}
		stage('deploy') {
			steps {
			    echo "TODO"
// 				sh '''
// 					docker-compose down --remove-orphans
// 					docker-compose build
// 					docker-compose up -d --remove-orphans
// 				'''
			}
		}
	}
}

