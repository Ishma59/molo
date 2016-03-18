import noop from 'lodash/noop';
import extend from 'lodash/extend';
import constant from 'lodash/constant';
import mapValues from 'lodash/mapValues';
import * as actions from 'src/views/git-importer/actions';
import { resolvesTo } from 'tests/utils';


function gitImporterFixtures(name) {
  switch (name) {
    case 'state':
      return {
        ui: {
          isLoading: false,
          currentStep: 'languages',
          lastStep: 'languages'
        },
        data: {
          sites: [{
            id: 'foo-id',
            name: 'foo'
          }, {
            id: 'bar-id',
            name: 'bar'
          }],
          site: {
            id: 'foo-id',
            name: 'foo'
          },
          languages: [{
            id: 'en',
            name: 'English',
            isMain: true,
            isChosen: false
          }, {
            id: 'sw',
            name: 'Swahili',
            isMain: false,
            isChosen: true
          }]
        }
      };


    case 'state-to-props':
      return {
        isLoading: false,
        languages: [{
          id: 'en',
          name: 'English',
          isMain: true,
          isChosen: false
        }, {
          id: 'sw',
          name: 'Swahili',
          isMain: false,
          isChosen: true
        }],
        site: {
          id: 'foo-id',
          name: 'foo'
        },
        sites: [{
          id: 'foo-id',
          name: 'foo'
        }, {
          id: 'bar-id',
          name: 'bar'
        }],
        steps: {
          site: {
            isDisabled: false,
            isExpanded: false
          },
          main: {
            isDisabled: false,
            isExpanded: false
          },
          languages: {
            isDisabled: false,
            isExpanded: true
          }
        }
      };


    case 'git-importer':
      return extend(gitImporterFixtures('state-to-props'), {
        actions: mapValues(actions, constant(noop))
      });


    case 'api':
      return {
        sites: resolvesTo([{
          id: 'foo-id',
          name: 'foo'
        }, {
          id: 'bar-id',
          name: 'bar'
        }]),
        languages: resolvesTo([{
          id: 'en',
          name: 'English',
          isMain: false,
          isChosen: false
        }, {
          id: 'sw',
          name: 'Swahili',
          isMain: false,
          isChosen: false
        }]),
        importContent: resolvesTo({
          errors: []
        })
      };
  }
}


export default gitImporterFixtures;
