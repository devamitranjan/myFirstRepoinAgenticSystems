# Database Concepts for AI Systems -- Questions

1.  **Explain why databases are important in real-world AI systems.**\
    Mention examples of the types of data typically stored in databases
    and why structured storage is necessary.

    Databases are critical in real-world AI systems because they provide reliable, scalable, and queryable storage for the large volumes of data that models depend on. They typically store user profiles, logs, transactions, sensor data, product catalogs, labels, and model predictions. Structured storage (tables with defined types and constraints) makes data consistent, easier to validate and clean, and much faster to filter, aggregate, and join than working with ad-hoc files, which improves both training data pipelines and production inference.

2.  **Describe the relational database mental model.**\
    Explain what tables, rows, and columns represent, and why each table
    should represent a single entity.

    In a relational database, we think in terms of tables that look like spreadsheets. Each table represents one type of entity (for example, `users` or `orders`). Each row is a single instance of that entity (one user, one order), and each column is an attribute of that entity (such as `email`, `created_at`, or `total_amount`). Keeping “one entity per table” avoids confusion and duplication, and makes it easier to express relationships across tables using keys and joins.

3.  **Explain the concept of a primary key.**\
    Describe why primary keys must be unique and non-null, and how they
    help identify records in a table.

    A primary key is a special column (or set of columns) whose value uniquely identifies each row in a table. It must be unique so that no two rows share the same identifier, and non-null so that every row is guaranteed to have an ID. Primary keys let both humans and the database engine reliably find, update, or delete exactly one record and are the main way other tables refer back to a specific row.

4.  **Explain what a database schema is.**\
    Describe what information a schema defines and why schemas are
    important for maintaining consistent data structure.

    A database schema is the formal definition of the structure of the data in a database. It specifies which tables exist, their columns, data types, constraints (like primary keys, foreign keys, and uniqueness), and sometimes indexes and default values. Schemas are important because they enforce consistent shapes and rules for data, preventing invalid or incomplete records and making sure that applications, ETL jobs, and AI pipelines can all rely on the same data structure over time.

5.  **Explain how relationships between tables work in relational
    databases.**\
    Describe the role of foreign keys and how tables such as `users` and
    `orders` can be connected.

    Relationships in relational databases are created by linking primary keys in one table to foreign keys in another. A foreign key is a column whose values must match an existing primary key value in the related table, which enforces referential integrity. For example, an `orders` table might have a `user_id` foreign key that points to the `id` primary key in the `users` table, so each order is associated with exactly one user and queries can easily join `users` and `orders` to answer questions like “which orders belong to this user?”.
