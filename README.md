In this repo I am learning and documenting how to make a Home Assistant Custom Integration. A few prequisites before you get started:
- You need to have Home Assistant installed. You can find instructions here: https://www.home-assistant.io/installation/
- Secondly, in your Home Assistant instance, you need to install the Home Assistant Community Store (HACS). This is carefully [explained here](https://www.home-assistant.io/blog/2024/08/21/hacs-the-best-way-to-share-community-made-projects/#how-to-install)

Once the above two prequisites are met, you should be able to open the HACS interface through http://IP:8123/hacs (for some http://homeassistant.local:8123/hacs should work).


# Adding the Custom Repository
The most right top button with the three dots is the menu button in the HACS interface. Click it and select "Custom Repositories". In the dialog that opens, you can add this repository (or any other of your liking) as a custom repository by simply pasting the GitHub URL (both the .git and non .git versions should work). For this repo you need to select "Integration" as the category.

The repository that you want to add is required to meet a few criteria before HACS will accept it. You can find the [criteria](https://hacs.xyz/docs/publish/integration):
```filetree
custom_components/INTEGRATION_NAME/__init__.py  // Of course, change INTEGRATION_NAME to your integration name
custom_components/INTEGRATION_NAME/PLATFORM_NAME.py  // Also, change PLATFORM_NAME to the type of integration you are making (e.g. light, sensor) more info: https://developers.home-assistant.io/docs/creating_platform_index/, or: https://www.home-assistant.io/integrations/?brands=featured
custom_components/INTEGRATION_NAME/manifest.json
README.md
hacs.json
```

Note that besides the structure, these files also need content. This repo provides a basic example. Also, you can also find more information in the corresponding files in this repo.

If you are interested in making your own custom integration, from here on you can follow [this video](https://www.youtube.com/watch?app=desktop&v=e3VwPb72Bbg). But of doing all of work directly in VS Code *on* HA, I recommend you make a repo and use the info we went through above.



