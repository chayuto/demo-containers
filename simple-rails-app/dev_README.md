sudo docker compose up --build


docker compose exec web rails console


Build snipplet 
```
brew upgrade ruby-build

rbenv install 3.3.4

rbenv local 3.3.4

gem install bundler

gem install rails

rails new myapp -d postgresql
```