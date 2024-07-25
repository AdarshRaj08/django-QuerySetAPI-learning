# Django QuerySet API Learning Repository

Welcome to my Django QuerySet API learning repository. This repository contains my notes and examples of using Django's QuerySet API, including field lookups, Q-objects, limiting QuerySets, and various QuerySet methods.

## Contents

1. [QuerySet API Methods](#queryset-api-methods)
   - Methods that return new QuerySets
   - Methods that do not return QuerySets
2. [Field Lookups](#field-lookups)
   - Simple function examples
   - Aggregate function examples
3. [Q-Objects and Limiting QuerySets](#q-objects-and-limiting-querysets)

## QuerySet API Methods

### Methods That Return New QuerySets

These methods can be chained together to refine the QuerySet:

- `filter()`
- `exclude()`
- `annotate()`
- `order_by()`
- `distinct()`
- `reverse()`
- `values()`
- `values_list()`
- `select_related()`
- `prefetch_related()`

### Methods That Do Not Return QuerySets

These methods are typically used to perform actions on the QuerySet or return specific data:

- `get()`
- `create()`
- `get_or_create()`
- `update_or_create()`
- `bulk_create()`
- `bulk_update()`
- `count()`
- `exists()`
- `update()`
- `delete()`

> **Note:** Detailed explanations and examples of each method can be found in the `views.py` file of the `app` directory.

## Field Lookups

Field lookups are used to specify conditions in QuerySets.

### Simple Function Examples

Examples of common field lookups:

- `exact`
- `iexact`
- `contains`
- `icontains`
- `in`
- `gt`
- `gte`
- `lt`
- `lte`
- `startswith`
- `istartswith`
- `endswith`
- `iendswith`
- `range`
- `isnull`
- `search`

### Aggregate Function Examples

Examples of using aggregate functions in QuerySets:

- `Sum`
- `Avg`
- `Max`
- `Min`
- `Count`

> **Note:** See the `views.py` file in the `fieldlookups` app for detailed examples of these functions.

## Q-Objects and Limiting QuerySets

### Q-Objects

Q-objects are used to build complex queries with logical operators (AND, OR, NOT).

- Combining conditions with `&` (AND)
- Combining conditions with `|` (OR)
- Negating conditions with `~` (NOT)

### Limiting QuerySets

Methods to limit the number of results returned by a QuerySet:

- `all()`
- `filter()`
- `exclude()`
- `order_by()`
- `distinct()`
- `reverse()`
- `values()`
- `values_list()`
- `select_related()`
- `prefetch_related()`

> **Note:** Detailed examples and usage of Q-objects and limiting QuerySets can be found in the `views.py` file of the `fieldlookups` app.

---

This repository is intended for educational purposes and to document my learning journey with Django's QuerySet API. Feel free to explore the examples and notes, and reach out if you have any questions or suggestions.

Happy Coding!
