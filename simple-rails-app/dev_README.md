sudo docker compose up --build


docker compose exec web ./bin/rails console

```
Loading production environment (Rails 7.1.3.4)
irb(main):001> 
```

Build snipplet 
```
brew upgrade ruby-build

rbenv install 3.3.4

rbenv local 3.3.4

gem install bundler

gem install rails

rails new myapp -d postgresql
```