pipeline {
    agent {
        node {
            label 'Muscle-Agent'
        }
    }

    options {
        timeout(time: 1, unit: 'HOURS')
        retry(1)
    }

    environment {
        POETRY_HOME = "${WORKSPACE}/.poetry"
        PATH = "${POETRY_HOME}/bin:${PATH}"
    }

    stages {

        stage('Check Environment') {
            steps {
                echo "check Python and Poetry is install"

                sh '''
                    python3 --version
                    poetry --version
                '''

            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies"
                sh '''
                poetry install --no-interaction --no-root
                '''
            }
            post {
                success{
                    echo "dependencies passed"
                }
                failure{
                    echo "dependencies failed"
                    sh 'tail -n 10 install_log.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests"
                sh '''
                export PYTHONPATH="${WORKSPACE}/src:$PYTHONPATH"
                mkdir -p test-reports
                 poetry run pytest --html=test-reports/report.html --self-contained-html 
                '''
            }
            post {
                always{
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'test-reports',
                        reportFiles: 'report.html',
                        reportName: 'Python Test Report'
                    ])
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building project"
                sh '''
                poetry build
                '''
            }
            post {
                success {
                    echo "Build completed"
                }
                failure{
                    echo "Build not completed"

                    sh 'tail -n 10 build_log.txt'
                }
            }
        }

        stage('artefacts') {
            steps {
                echo 'Generating artefacts'

                sh '''
                    mkdir -p artifacts/ 
                    cp -r dist/ artifacts/ 2>/dev/null
                    cp -r test-reports/ artifacts/ 2>/dev/null
                    find artifacts/ -type f
                '''
            }
            post {
                always {
                     archiveArtifacts artifacts: 'artifacts/**/*', fingerprint: true
                }
            }
        }
    }   
}