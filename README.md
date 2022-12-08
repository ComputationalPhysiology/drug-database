[![MIT](https://img.shields.io/github/license/ComputationalPhysiology/drug-database)](https://github.com/ComputationalPhysiology/drug-database/blob/main/LICENSE)
[![Test package](https://github.com/ComputationalPhysiology/drug-database/actions/workflows/main.yml/badge.svg)](https://github.com/ComputationalPhysiology/drug-database/actions/workflows/main.yml)
[![pre-commit](https://github.com/ComputationalPhysiology/drug-database/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/ComputationalPhysiology/drug-database/actions/workflows/pre-commit.yml)
[![Deploy static content to Pages](https://github.com/ComputationalPhysiology/drug-database/actions/workflows/build_docs.yml/badge.svg)](https://github.com/ComputationalPhysiology/drug-database/actions/workflows/build_docs.yml)

# Drug database
Simple command line interface for getting scaling factors for different drugs

Documentation: https://ComputationalPhysiology.github.io/drug-database/
Source code: https://github.com/ComputationalPhysiology/drug-database

## Install
```
$ python -m pip install drug-database
```
Once installed you will get access to the `drug-db` command.

## Usage
Get help using
```
$ drug-db --help
```

### List all available drugs
```
$ drug-db list-drugs
    Drugs
┏━━━━━━━━━━━━━━━━┓
┃           Name ┃
┡━━━━━━━━━━━━━━━━┩
│        Sotalol │
│      Azimilide │
│      Ibutilide │
│    Risperidone │
│ Clarithromycin │
│    Terfenadine │
│       Bepridil │
│       Pimozide │
│     Dofetilide │
│   Disopyramide │
│      Cisapride │
│      Tamoxifen │
│     Vandetanib │
│     Metropolol │
│     Droperidol │
│     Loratadine │
│     Ranolazine │
│      Quinidine │
│      Diltiazem │
│     Astemizole │
│   Nitrendipine │
│ Chlorpromazine │
│      Clozapine │
│        Control │
│     Nifedipine │
│      Verapamil │
│    Domperidone │
│    Ondansetron │
│     Mexiletine │
└────────────────┘
```

### Showing information about specific drug
```
$ drug-db show-drug Verapamil
   Scaling factors for drug
     Verapamil and FPC 1
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃              Name ┃ Value  ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    scale_drug_INa │ 1.0    │
│   scale_drug_INaL │ 1.0    │
│    scale_drug_Ito │ 1.0    │
│   scale_drug_ICaL │ 0.7342 │
│    scale_drug_IKr │ 0.8815 │
│    scale_drug_IKs │ 1.0    │
│    scale_drug_IK1 │ 1.0    │
│    scale_drug_IKb │ 1.0    │
│   scale_drug_INab │ 1.0    │
│   scale_drug_ICab │ 1.0    │
│   scale_drug_IpCa │ 1.0    │
│ scale_drug_Isacns │ 1.0    │
│  scale_drug_Isack │ 1.0    │
└───────────────────┴────────┘
```

Note that this is showing the values that are 1 times FPC (FIXME: explain what this means). If you want to get the values for 5 times FPC the you can do
```
$ drug-db show-drug Verapamil --fpc 5
   Scaling factors for drug
     Verapamil and FPC 5
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃              Name ┃ Value  ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│    scale_drug_INa │ 1.0    │
│   scale_drug_INaL │ 0.9997 │
│    scale_drug_Ito │ 1.0    │
│   scale_drug_ICaL │ 0.3199 │
│    scale_drug_IKr │ 0.5588 │
│    scale_drug_IKs │ 1.0    │
│    scale_drug_IK1 │ 1.0    │
│    scale_drug_IKb │ 1.0    │
│   scale_drug_INab │ 1.0    │
│   scale_drug_ICab │ 1.0    │
│   scale_drug_IpCa │ 1.0    │
│ scale_drug_Isacns │ 1.0    │
│  scale_drug_Isack │ 1.0    │
└───────────────────┴────────┘
```

### json support
By default the tables are displayed in a [Rich table](https://rich.readthedocs.io/en/stable/tables.html), however sometimes you might want to use these values in another program in which you can convert the values to json by using the `--json` flag, e.g
```
$ drug-db show-drug Verapamil --fpc 5 --json
{"scale_drug_INa": 1.0, "scale_drug_INaL": 0.9997, "scale_drug_Ito": 1.0, "scale_drug_ICaL": 0.3199, "scale_drug_IKr": 0.5588, "scale_drug_IKs": 1.0, "scale_drug_IK1": 1.0, "scale_drug_IKb": 1.0,
"scale_drug_INab": 1.0, "scale_drug_ICab": 1.0, "scale_drug_IpCa": 1.0, "scale_drug_Isacns": 1.0, "scale_drug_Isack": 1.0}
```
You can also save this to a file using e.g
```
$ drug-db show-drug Verapamil --fpc 5 --json > verapamil_5.json
```


## License
MIT

## Author
Henrik Finsberg (henriknf@simula.no)
