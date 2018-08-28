query_temp = '''<?xml version="1.0"?>
<!DOCTYPE PCT-Data PUBLIC "-//NCBI//NCBI PCTools/EN" "http://pubchem.ncbi.nlm.nih.gov/pug/pug.dtd">
<PCT-Data>
  <PCT-Data_input>
    <PCT-InputData>
      <PCT-InputData_query>
        <PCT-Query>
          <PCT-Query_type>
            <PCT-QueryType>
              <PCT-QueryType_css>
                <PCT-QueryCompoundCS>
                  <PCT-QueryCompoundCS_query>
                    <PCT-QueryCompoundCS_query_data>%(query)s</PCT-QueryCompoundCS_query_data>
                  </PCT-QueryCompoundCS_query>
                  <PCT-QueryCompoundCS_type>
                    <PCT-QueryCompoundCS_type_identical>
                      <PCT-CSIdentity value="same-isotope">4</PCT-CSIdentity>
                    </PCT-QueryCompoundCS_type_identical>
                  </PCT-QueryCompoundCS_type>
                  <PCT-QueryCompoundCS_results>100</PCT-QueryCompoundCS_results>
                </PCT-QueryCompoundCS>
              </PCT-QueryType_css>
            </PCT-QueryType>
          </PCT-Query_type>
        </PCT-Query>
      </PCT-InputData_query>
    </PCT-InputData>
  </PCT-Data_input>
</PCT-Data>
'''

import urllib2
site = "http://pubchem.ncbi.nlm.nih.gov/pug/pug.cgi"

import time
import re

query = query_temp % {"query": "c1ccccc1C"}
f = urllib2.urlopen( site, query)
out = f.read()
f.close()
print out
