{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMoS+y4No6bdG9Wq3Xg9Wgo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC110C.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SMSAEn1dNFW7"
      },
      "outputs": [],
      "source": [
        "s = input()\n",
        "t = input()\n",
        "\n",
        "change = {}\n",
        "\n",
        "used = set()\n",
        "flag = True\n",
        "for i in range(len(s)):\n",
        "  if S[i] not in change:\n",
        "    if T[i] in used:\n",
        "      flag = False\n",
        "      break\n",
        "    change[s[i]] = T[i]\n",
        "    used.add(T[i])\n",
        "  else:\n",
        "    if change[s[i]] != T[i]:\n",
        "      flag = False\n",
        "      break\n",
        "\n",
        "print(\"Yes\" if flag else \"No\")\n",
        "\n",
        "\n",
        "# reで落ちる\n",
        " "
      ]
    }
  ]
}