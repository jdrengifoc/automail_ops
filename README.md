# automail_ops

This project divides in four parts.

1. **Credentials manajement.** Create two files: `collaborators.json` and `collaborators.parquet`, where are stored the credentials of the collaborators. This file must have the following properties.

    * Each credential is composed of the fields:
        * `id`: Unique inmutable identifier per user.
        * `send2folder`: Unique mutable folder where the collaborator's stagged files are stored.
        * `name`: Unique (case unsensitive) mutable name of the collaborator.
        * `email`: Unique (case unsensitive) mutable email of the collaborator.
        * `allowed_folders`: Mutable folders paths where the collaborator have full access.
        * `allowed_files`: Mutable specific files to which the collaborator have access.
    
    * All fields are enter by a manager except the `id` and `send2folder`.
    
    * A credential is in the database iff:
        * Have valid credentials. That means that the `email` has a valid structure and is derivable, and the paths exists.
        * Is unique for `id`, `name` and `email` separatly.

    * A existing credential can be updated in the mutable fields. So the access must be by `id`.
    
2. **Log history storage**: Dataset with the 


## Useful links
* [A sample Python project](https://github.com/pypa/sampleproject)