# Informfully Datasets

![Informfully](https://raw.githubusercontent.com/Informfully/Documentation/main/docs/source/img/logo_banner.png)

Welcome to Informfully ([GitHub](https://github.com/orgs/Informfully) & [Website](https://informfully.ch/))!
Informfully is an open-source reproducibility platform for content distribution and user experiments.

**Links and Resources:** [GitHub](https://github.com/orgs/Informfully) | [Website](https://informfully.ch) | [X](https://x.com/informfully) | [Documentation](https://informfully.readthedocs.io) | [DDIS@UZH](https://www.ifi.uzh.ch/en/ddis.html) | [Google Play](https://play.google.com/store/apps/details?id=ch.uzh.ifi.news) | [App Store](https://apps.apple.com/us/app/informfully/id1460234202)

## Overview

The Informfully Dataset with Enhanced Attributes (IDEA) for news articles.
Recommendations consist of an open-source collection of user profiles, news articles with a high topic and outlet diversity, item recommendations, and rich user-item interactions from a field study on behavioral changes in news consumption.
The records include both quantitative data from real-time session tracking as well as self-reported data from user surveys on satisfaction with news, knowledge
acquisition, and personal background information. This paper outlines the data collection procedure and potential use cases of the dataset for designing normative recommender systems.
It provides the
documentation of all data collections, together with insights into the data quality.

Get access to the full paper here: [IDEA - Informfully Dataset with Enhanced Attributes](https://ceur-ws.org/Vol-3898/paper1.pdf)

## Documentation

* [IDEA – Informfully Dataset with Enhanced Attributes](https://ceur-ws.org/Vol-3898/paper1.pdf) workshop paper.
* [Dataset codebook](https://github.com/Informfully/Datasets/blob/main/IDEA/Codebook.pdf) for the description of all attributes included in the dataset.
* [Pre-processing scripts](https://github.com/Informfully/Datasets/tree/main/IDEA/scripts) used for creating the individual files shared in the dataset.
* [Technical documentation](https://informfully.readthedocs.io/en/latest/database.html) of outlining all document collections from Informfully.
* [Experiment pre-registration 1](https://osf.io/yp5d9?mode=&revisionId=&view_only=) for information related to the first week.
* [Experiment pre-registration 2](https://osf.io/cqebd?mode=&revisionId=&view_only=) for information related to the second week.

## Dataset

| Collection      | Description                           | # Entries |
|-----------------|---------------------------------------|-----------|
| Articles        | News article collection.              | *10,954*  |
| Bookmarks       | Bookmarked news articles.             | *2,479*   |
| Favorites       | Favorites news articles.              | *3,115*   |
| Interactions    | Read articles by users.               | *34,890*  |
| Ratings         | Likes and dislikes for articles.      | *28,382*  |
| Recommendations | Daily article recommendations.        | *207,220* |
| Survey          | Knowledge quiz answers.               | *43,078*  |
| Users           | Profile and background information.   | *593*     |
| Views           | Browsing and session history.         | *84,747*  |

If you are looking for more news datasets, we recommend the following resources:

* [Adressa](https://reclab.idi.ntnu.no/dataset)
* [EB-NeRD](https://recsys.eb.dk)
* [Globo](https://www.kaggle.com/datasets/joelpl/news-portal-recommendations-npr-by-globo)
* [NeMig](https://github.com/andreeaiana/nemig)
* [MIND](https://msnews.github.io)

## Citation

If you use any code or data from this repository in a scientific publication, we ask you to cite the following papers:

- [IDEA – Informfully Dataset with Enhanced Attributes](https://ceur-ws.org/Vol-3898/paper1.pdf), Heitz *et al.*, Proceedings of the Second Workshop on the Normative Design and Evaluation of Recommender Systems, 2024.

  ```
  @inproceedings{heitz2024idea,
    title={IDEA – Informfully Dataset with Enhanced Attributes},
    author={Heitz, Lucien and Mattis, Nicolas and Inel, Oana and van Atteveldt, Wouter},
    booktitle={Proceedings of the Second Workshop on the Normative Design and Evaluation of Recommender Systems},
    year={2024}
  }
  ```

- [Informfully - Research Platform for Reproducible User Studies](https://dl.acm.org/doi/10.1145/3640457.3688066), Heitz *et al.*, Proceedings of the 18th ACM Conference on Recommender Systems, 2024.

  ```
  @inproceedings{heitz2024informfully,
    title={Informfully - Research Platform for Reproducible User Studies},
    author={Heitz, Lucien and Croci, Julian A and Sachdeva, Madhav and Bernstein, Abraham},
    booktitle={Proceedings of the 18th ACM Conference on Recommender Systems},
    pages={660--669},
    year={2024}
  }
  ```

## Contributing

You are welcome to contribute to the Informfully ecosystem and become a part of our community. Feel free to:
  - fork any of the [Informfully repositories](https://github.com/Informfully)
  - join and write on the [discussion board](https://github.com/orgs/Informfully/discussions)
  - make changes and create pull requests

Please post your feature requests and bug reports in our [GitHub issues](https://github.com/Informfully/Documentation/issues) section.

## License

Released under the [MIT License](LICENSE). (Please note that the respective copyright licenses of third-party libraries and dependencies apply.)

![Screenshots](https://raw.githubusercontent.com/Informfully/Documentation/main/docs/source/img/app_screens.png)
