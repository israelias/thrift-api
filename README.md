


# Thrift API 
DJ-DRF Models and Serverless ETL Functions using Vercel's Python Runtime.

This is serves [israelias/thrift-fe](https://github.com/israelias/django-react-ecommerce/tree/master/frontend)

## `@todo` 
`git config --global --unset https.proxy`
`git config --global --unset http.proxy`

```python
pip install wheel setuptools pip --upgrade
pip3 install wheel setuptools pip --upgrade
```
 pip list --format=freeze > requirementss.txt
--use-deprecated=legacy-resolver
This is a migration.

Python has been installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /opt/homebrew/opt/python@3.10/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /opt/homebrew/lib/python3.10/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.10

See: https://docs.brew.sh/Homebrew-and-Python
==> Summary
🍺  /opt/homebrew/Cellar/python@3.10/3.10.9: 3,110 files, 57.1MB
==> Running `brew cleanup python@3.10`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> python@3.10
Python has been installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /opt/homebrew/opt/python@3.10/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /opt/homebrew/lib/python3.10/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.10

See: https://docs.brew.sh/Homebrew-and-Python

--use-deprecated=legacy-resolver --use-pep517


- [ ] Factory Data
- [ ] Testing 
- [ ] User, UserProfile, Favorites, Cart, classes
- [ ] Vendor, VendorProfile, Favorites/Orders, Products/Cart classes
- [ ] Routes GraphQL/REST

```python
urlpatterns_root = [
    path("", include("account.urls", namespace="account")),
    path("", include("store.urls", namespace="store")),
    path("", include("vendor.urls", namespace="vendor")),
    path("", include("order.urls", namespace="order")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True)))),
    url(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    url(r"^api/", include(urlpatterns_root)),
]

```


#### Stripe
Stripe makes it easy to be PCI compliant. With a proper integration, you will never have access to your customers' payment information.

A typical payment flow with Stripe can be divided in two steps:

Collect the customer's payment information, using the prebuilt [Checkout form](https://stripe.com/docs/payments/checkout), or a form of your own using [Stripe.js](https://stripe.com/docs/js).

In both cases, the card information is sent directly from the customer's browser to Stripe's servers, which return a [card token](https://stripe.com/docs/api/tokens/object). You then send this token to your backend.

On your backend, you use the token to [create a charge](https://stripe.com/docs/api/charges/create).

The token represents a card, but hides the PCI sensitive information (i.e. the whole card number and the CVC) from you.

You can find a simple tutorial for creating charges [here](https://stripe.com/docs/payments/charges-api).

If you don't plan on charging the same customer multiple times (or if you don't mind asking them to provide their card information every time), then you don't necessarily need to store anything in your own database. When you create the charge, you will be immediately informed of the result (success or failure) and can take the necessary actions.

## References
- [Using PathLib](https://adamj.eu/tech/2020/03/16/use-pathlib-in-your-django-project/)
- [Categories with django-mptt](https://djangopy.org/package-of-week/categories-with-django-mptt/)
- [Django-Rest Flex-Fields](https://github.com/rsinger86/drf-flex-fields#query-optimization-experimental)
- [DRF-YASG: Yet Another Swagger Generator](https://github.com/axnsan12/drf-yasg/)
- [DRF: ReDoc](https://github.com/Redocly/redoc)
- [Documenting your API using Open API (Swagger) and Redoc in Django Rest Framework.](https://medium.com/@torkashvand/)
- [Django REST Framework combining routers from different apps](https://stackoverflow.com/questions/31483282/django-rest-framework-combining-routers-from-different-apps)
- [Sebastien Mirolo: Documenting an API implemented with Django Rest Framework](https://www.djaodjin.com/blog/django-rest-framework-api-docs.blog)
- [DRF: Filtering](https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-current-user)
- [DRF: SerializerMethodField](https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield)
- [DRF: Database Functions](https://docs.djangoproject.com/en/3.2/ref/models/database-functions/)
- [DRF: Create Profile with User via Signals](https://stackoverflow.com/questions/33659994/django-rest-framework-create-user-and-user-profile)
- [DRF: Signals](https://docs.djangoproject.com/en/3.2/topics/signals/)
- [Django-Storages with AWS S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
- [Django: Email Host](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-EMAIL_HOST)
- [Resizing Images on upload](https://www.reddit.com/r/django/comments/99za8t/resizing_images_on_upload_is_there_any_reason_i/)
- [Django-VersatileImageField](https://django-versatileimagefield.readthedocs.io/en/latest)
- [Django-VersatileImageField: Improving Performance](https://django-versatileimagefield.readthedocs.io/en/latest/improving_performance.html)
- [Django: ROOT_URLCONF, MEDIAL_ROOT and STATIC_URL](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-ROOT_URLCONF)
- [Django: DEFAULT_FILE_STORAGE and STATICFILES_DIRS](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEFAULT_FILE_STORAGE)
- [Adam Johnson: Use Pathlib in Your Django Settings File (Django ^3.1)](https://adamj.eu/tech/2020/03/16/use-pathlib-in-your-django-project/)
- [Create Custom Exception Handler](https://djangocircle.com/create-custom-exception-handler-django-rest-api/)
- [Creating a Django API using Django Rest Framework APIView](https://medium.com/the-andela-way/creating-a-django-api-using-django-rest-framework-apiview-b365dca53c1d)
- [Django Internationalization/Localization](https://docs.djangoproject.com/en/3.2/topics/i18n/)
- [CORS guide](https://www.stackhawk.com/blog/django-cors-guide/)
- [Python `del` syntax](https://www.geeksforgeeks.org/python-del-to-delete-objects/)