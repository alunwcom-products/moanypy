pipeline {
	agent any
	triggers {
		pollSCM('H/2 * * * *')
	}
	options {
		buildDiscarder(logRotator(numToKeepStr: '7'))
	}
	stages {
		stage('init') {
			steps {
				echo "Using workspace [${WORKSPACE}]"
				echo "Branch = ${env.BRANCH_NAME}"
			}
		}
		stage('build') {
			steps {
				echo "Git commit = ${GIT_COMMIT}"
				sh '''
				    git checkout ${BRANCH_NAME}

				    VERSION=$(git describe --dirty --always)
				    echo "VERSION=${VERSION}"
					docker build -t alunwcom/moanypy:latest -f Dockerfile .
				'''
				echo "Version = ${env.VERSION}"
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

