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

				checkout([$class: 'GitSCM',
                    branches: [[name: env.BRANCH_NAME ]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'CleanCheckout']],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: 'https://github.com/user/repo.git']]
])
			}
		}
		stage('build') {
			steps {
				echo "Git commit = ${GIT_COMMIT}"
				sh '''
				    VERSION=$(git describe)
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

