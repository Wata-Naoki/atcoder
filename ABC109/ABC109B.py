{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOyPw0B8bUc80RNVV/ajIXD",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC109B.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L_0AehF__nNy",
        "outputId": "9d8eb1c3-7d03-46b0-c044-20209af89630"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "hoge\n",
            "english\n",
            "sisi\n",
            "No\n"
          ]
        }
      ],
      "source": [
        "input_line = int(input())\n",
        "\n",
        "ans_list = []\n",
        "flag = True\n",
        "\n",
        "for i in range(input_line):\n",
        "    s = input()\n",
        "    if s in ans_list:\n",
        "      flag = False\n",
        "      break\n",
        "    ans_list.append(s)\n",
        "    if i > 0:\n",
        "      if ans_list[i][0] != ans_list[i-1][-1]:\n",
        "        flag = False\n",
        "        break\n",
        "\n",
        "print('Yes' if flag else 'No')\n",
        "\n",
        " \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# g = ['str', 'int']\n",
        "\n",
        "# print(g[0][0])\n",
        "\n",
        "# a = 'str'\n",
        "# print(a[-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VijCDhqFD7w-",
        "outputId": "56316f3a-df34-40fa-9562-eb902b7fc5f2"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "r\n"
          ]
        }
      ]
    }
  ]
}