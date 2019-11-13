# elastic-template-cloner

Uitlity for moving templates across clusters


Basic usage
- all templates are space seperated

elastic-template-cloner.py --origin http://origin-host:9200 --destination http://destination-host:9200 --templates templateA templateB etc

If you want to append a prefix to the template in destination template

elastic-template-cloner.py --origin http://origin-host:9200 --destination http://destination-host:9200 --prefix new --templates templateA templateB etc


