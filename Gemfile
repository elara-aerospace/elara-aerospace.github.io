source 'https://rubygems.org'

# Using static site generator software
gem 'jekyll', '~> 3.10.0'

# If you want to use GitHub Pages, remove the "gem 'jekyll'" above and uncomment the line below. To upgrade, run `bundle update github-pages`.
gem 'github-pages', '~> 232', group: :jekyll_plugins
gem 'github-pages-health-check', '~> 1.18.2'
gem 'webrick', '~> 1.9'

# If you have any plugins, put them here!
group :jekyll_plugins do
  gem 'jekyll-sitemap', '~> 1.4.0'
  gem 'jekyll-feed', '~> 0.17.0'
  gem 'jekyll-seo-tag', '~> 2.8.0'
  gem 'jekyll-mentions', '~> 1.6.0'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem 'tzinfo', '~> 2.0', '>= 2.0.6'
  gem 'tzinfo-data', '~> 1.2024', '>= 1.2024.1'
end

# Performance-booster for watching directories on Windows
gem 'wdm', '~> 0.1.1', :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem do not have a Java counterpart.
gem 'http_parser.rb', '~> 0.6.0', :platforms => [:jruby]

# A secure, non-evaling end user template engine with aesthetic markup
gem 'liquid', '~> 4.0.4'

# Check-up Tests
gem 'html-proofer', '~> 5.0'
gem 'rake', '~> 13.2', '>= 13.2.1'
gem 'minitest', '~> 5.25'

# Performance
gem 'jekyll-loading-lazy'


gem "faraday-retry", "~> 2.3"

gem "image_optim", "~> 0.31.4"
gem "image_optim_pack", "~> 0.12.1"
