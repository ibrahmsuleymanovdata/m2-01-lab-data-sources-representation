{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a57b809e-e3c3-4089-986b-5e7365013532",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[22.5, None, 31.0, None, -5.0, None]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw_inputs = [\"22.5\", \"not a number\", \"31\", \"\", \"-5.0\", \"27.3°C\"]\n",
    "\n",
    "parsed = []\n",
    "for entry in raw_inputs:\n",
    "    try:\n",
    "        value = float(entry)\n",
    "        parsed.append(value)\n",
    "    except ValueError:\n",
    "        parsed.append(None)\n",
    "\n",
    "parsed\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fe11420c-a316-4fe0-8f4e-e3fb9a4d5066",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"timestamp\": \"2026-03-02T09:46:30.780532\",\n",
      "  \"service\": \"recommendation-engine\",\n",
      "  \"event\": \"prediction_served\",\n",
      "  \"user_id\": \"u-38291\",\n",
      "  \"latency_ms\": 47,\n",
      "  \"model_version\": \"v2.3.1\"\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "from datetime import datetime\n",
    "\n",
    "log_entry = {\n",
    "    \"timestamp\": datetime.now().isoformat(),\n",
    "    \"service\": \"recommendation-engine\",\n",
    "    \"event\": \"prediction_served\",\n",
    "    \"user_id\": \"u-38291\",\n",
    "    \"latency_ms\": 47,\n",
    "    \"model_version\": \"v2.3.1\"\n",
    "}\n",
    "\n",
    "print(json.dumps(log_entry, indent=2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1a74eb80-264a-43ce-bf38-4680b0eb7717",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"name\": \"Boatie McBoatFace\",\n",
      "  \"age\": 12,\n",
      "  \"is_active\": true,\n",
      "  \"address\": {\n",
      "    \"street\": \"12 Ocean Drive\",\n",
      "    \"city\": \"Port Royal\",\n",
      "    \"postal_code\": \"10021-3100\"\n",
      "  },\n",
      "  \"tags\": [\n",
      "    \"marine\",\n",
      "    \"research\",\n",
      "    \"autonomous\"\n",
      "  ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "record = {\n",
    "    \"name\": \"Boatie McBoatFace\",\n",
    "    \"age\": 12,\n",
    "    \"is_active\": True,\n",
    "    \"address\": {\n",
    "        \"street\": \"12 Ocean Drive\",\n",
    "        \"city\": \"Port Royal\",\n",
    "        \"postal_code\": \"10021-3100\"\n",
    "    },\n",
    "    \"tags\": [\"marine\", \"research\", \"autonomous\"]\n",
    "}\n",
    "\n",
    "serialized = json.dumps(record, indent=2)\n",
    "print(serialized)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f2a3ab0c-6e4d-4a06-a61a-c4c3fe3ecf7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"text\": \"Boatie McBoatFace, aged 12, active, at 12 Ocean Drive, Port Royal, 10021-3100, tags: marine research autonomous\"\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "blob = {\n",
    "    \"text\": \"Boatie McBoatFace, aged 12, active, at 12 Ocean Drive, Port Royal, 10021-3100, tags: marine research autonomous\"\n",
    "}\n",
    "\n",
    "print(json.dumps(blob, indent=2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ea6ce289-1da7-4153-a95e-17d3eb107839",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "city,temperature_c,humidity\n",
      "Seoul,26.5,0.60\n",
      "Berlin,18.2,0.65\n",
      "Nairobi,22.1,0.58\n",
      "Toronto,16.7,0.70\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import io\n",
    "\n",
    "data = [\n",
    "    [\"city\", \"temperature_c\", \"humidity\"],\n",
    "    [\"Seoul\", \"26.5\", \"0.60\"],\n",
    "    [\"Berlin\", \"18.2\", \"0.65\"],\n",
    "    [\"Nairobi\", \"22.1\", \"0.58\"],\n",
    "    [\"Toronto\", \"16.7\", \"0.70\"],\n",
    "]\n",
    "\n",
    "output = io.StringIO()\n",
    "writer = csv.writer(output)\n",
    "writer.writerows(data)\n",
    "csv_text = output.getvalue()\n",
    "print(csv_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "99bd002b-de6d-462f-9c4c-7e41d14693c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 4])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "a = np.array([[1,2,3],\n",
    "              [4,5,6]],order='F')\n",
    "\n",
    "a[:,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0723ef2c-9a2f-4a58-9491-c83bbd8a3149",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row 0: [1 2 3]\n",
      "Col 0: [1 4 7]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Create a small 2D array (row-major by default)\n",
    "arr = np.array([\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "])\n",
    "\n",
    "# Accessing a row is fast (contiguous in memory)\n",
    "print(\"Row 0:\", arr[0])\n",
    "\n",
    "# Accessing a column requires skipping elements\n",
    "print(\"Col 0:\", arr[:, 0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "921525f4-4c86-471f-9a41-b4c9e9aa620e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Memory layout (C = row-major): Row-major\n"
     ]
    }
   ],
   "source": [
    "print(\"Memory layout (C = row-major):\", \"Row-major\" if arr.flags['C_CONTIGUOUS'] else \"Column-major\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c08d3579-bdbc-4f21-aeaa-43fd26b089b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Column-major layout: Yes\n"
     ]
    }
   ],
   "source": [
    "# Column-major (Fortran-style) layout\n",
    "arr_col = np.array([\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "], order='F')\n",
    "\n",
    "print(\"Column-major layout:\", \"Yes\" if arr_col.flags['F_CONTIGUOUS'] else \"No\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7c95a45a-f896-4adf-9f02-bcc46a2b4c1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Create a DataFrame with 100,000 rows and 10 columns\n",
    "n_rows = 100_000\n",
    "df = pd.DataFrame(np.random.randn(n_rows, 10), columns=[f\"col_{i}\" for i in range(10)])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "def30bae-636b-4b8d-854e-e0e03fb5c689",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        0.214723\n",
       "1        1.660789\n",
       "2        0.509272\n",
       "3       -1.291297\n",
       "4        1.159401\n",
       "           ...   \n",
       "99995   -0.841117\n",
       "99996    0.213918\n",
       "99997    0.743785\n",
       "99998   -0.236738\n",
       "99999    2.328830\n",
       "Name: col_0, Length: 100000, dtype: float64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Column access: fast (contiguous memory)\n",
    "col_values = df[\"col_0\"]\n",
    "col_values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e1f14da0-1d16-4ed0-b9c2-754e1c8738ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 7 bytes\n",
      "Binary (int32): 4 bytes\n",
      "Space saved: 3 bytes (43%)\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "# Text representation of a number\n",
    "text_repr = \"1000000\"\n",
    "text_bytes = len(text_repr.encode('utf-8'))\n",
    "\n",
    "# Binary representation as a 32-bit integer\n",
    "import struct\n",
    "binary_repr = struct.pack('i', 1000000)\n",
    "binary_bytes = len(binary_repr)\n",
    "\n",
    "print(f\"Text: {text_bytes} bytes\")\n",
    "print(f\"Binary (int32): {binary_bytes} bytes\")\n",
    "print(f\"Space saved: {text_bytes - binary_bytes} bytes ({(1 - binary_bytes/text_bytes)*100:.0f}%)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "daa33b85-1561-489b-adb2-2bba2ad60f2c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "32a3dd5a-5de9-4929-8be6-999a784af147",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "user_id     int64\n",
      "name       object\n",
      "age         int64\n",
      "email      object\n",
      "dtype: object\n",
      "\n",
      "   user_id     name  age                email\n",
      "0      101    Alice   29    alice@example.com\n",
      "1      102      Bob   34      bob@example.com\n",
      "2      103  Charlie   41  charlie@example.com\n",
      "3      104    Diana   26    diana@example.com\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Structured data: clear schema, predictable types\n",
    "users = pd.DataFrame({\n",
    "    \"user_id\": [101, 102, 103, 104],\n",
    "    \"name\": [\"Alice\", \"Bob\", \"Charlie\", \"Diana\"],\n",
    "    \"age\": [29, 34, 41, 26],\n",
    "    \"email\": [\"alice@example.com\", \"bob@example.com\", \"charlie@example.com\", \"diana@example.com\"]\n",
    "})\n",
    "\n",
    "print(users.dtypes)\n",
    "print()\n",
    "print(users)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "94b8855a-9424-4f6a-acd3-73501aac6837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average age: 32.5\n"
     ]
    }
   ],
   "source": [
    "print(f\"Average age: {users['age'].mean():.1f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "21050618-bd0b-4e4b-8a86-8511d2b5e7af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'2025-03-15 10:23:45 INFO recommendation-engine prediction served for user u-38291 in 47ms'\n",
      "'2025-03-15 10:23:46 WARNING inventory-service stock check timeout for SKU-8832'\n",
      "'2025-03-15 10:23:47 INFO recommendation-engine prediction served for user u-10442 in 31ms'\n",
      "'2025-03-15 10:23:48 ERROR payment-gateway transaction failed: insufficient funds for order ORD-9921'\n"
     ]
    }
   ],
   "source": [
    "raw_logs = \"\"\"\n",
    "2025-03-15 10:23:45 INFO recommendation-engine prediction served for user u-38291 in 47ms\n",
    "2025-03-15 10:23:46 WARNING inventory-service stock check timeout for SKU-8832\n",
    "2025-03-15 10:23:47 INFO recommendation-engine prediction served for user u-10442 in 31ms\n",
    "2025-03-15 10:23:48 ERROR payment-gateway transaction failed: insufficient funds for order ORD-9921\n",
    "\"\"\"\n",
    "\n",
    "for line in raw_logs.strip().split(\"\\n\"):\n",
    "    print(repr(line))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5efbfcf5-4d4c-4958-a596-552f6abb202f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'timestamp': '2025-03-15 10:23:45', 'level': 'INFO', 'service': 'recommendation-engine', 'message': 'prediction served for user u-38291 in 47ms'}\n",
      "{'timestamp': '2025-03-15 10:23:46', 'level': 'WARNING', 'service': 'inventory-service', 'message': 'stock check timeout for SKU-8832'}\n",
      "{'timestamp': '2025-03-15 10:23:47', 'level': 'INFO', 'service': 'recommendation-engine', 'message': 'prediction served for user u-10442 in 31ms'}\n",
      "{'timestamp': '2025-03-15 10:23:48', 'level': 'ERROR', 'service': 'payment-gateway', 'message': 'transaction failed: insufficient funds for order ORD-9921'}\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "pattern = r\"(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}) (\\w+) (\\S+) (.+)\"\n",
    "parsed_logs = []\n",
    "\n",
    "for line in raw_logs.strip().split(\"\\n\"):\n",
    "    match = re.match(pattern, line)\n",
    "    if match:\n",
    "        parsed_logs.append({\n",
    "            \"timestamp\": match.group(1),\n",
    "            \"level\": match.group(2),\n",
    "            \"service\": match.group(3),\n",
    "            \"message\": match.group(4),\n",
    "        })\n",
    "\n",
    "for entry in parsed_logs:\n",
    "    print(entry)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "52552bf0-61b4-45f6-b0f7-8e27ca70d357",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['47', '31']\n"
     ]
    }
   ],
   "source": [
    "raw_logs = \"\"\"\n",
    "2025-03-15 10:23:45 INFO recommendation-engine prediction served for user u-38291 in 47ms\n",
    "2025-03-15 10:23:46 WARNING inventory-service stock check timeout for SKU-8832\n",
    "2025-03-15 10:23:47 INFO recommendation-engine prediction served for user u-10442 in 31ms\n",
    "2025-03-15 10:23:48 ERROR payment-gateway transaction failed: insufficient funds for order ORD-9921\n",
    "\"\"\"\n",
    "ms_values = re.findall(r'(\\d+)ms', raw_logs)\n",
    "\n",
    "print(ms_values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "100835e8-5c61-49b3-8acc-6c03ae2df21a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Type: click, Fields: ['event_type', 'timestamp', 'element', 'page']\n",
      "  Type: scroll, Fields: ['event_type', 'timestamp', 'depth_percent']\n",
      "  Type: click, Fields: ['event_type', 'timestamp', 'element', 'submenu']\n"
     ]
    }
   ],
   "source": [
    "events = [\n",
    "    {\"event_type\": \"click\", \"timestamp\": \"2025-03-15T10:23:45\", \"element\": \"buy_button\", \"page\": \"/product/123\"},\n",
    "    {\"event_type\": \"scroll\", \"timestamp\": \"2025-03-15T10:23:47\", \"depth_percent\": 75},\n",
    "    {\"event_type\": \"click\", \"timestamp\": \"2025-03-15T10:23:50\", \"element\": \"nav_menu\", \"submenu\": \"categories\"},\n",
    "]\n",
    "\n",
    "for event in events:\n",
    "    print(f\"  Type: {event['event_type']}, Fields: {list(event.keys())}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0213462c-2b24-488d-93d2-4a9641482289",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50948b46-1898-4ebc-80a2-3da4f0e7ef33",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4154cf2a-9953-4966-a49b-db45b2258b87",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dfbe5bad-4851-4e2a-979e-46fad10d2e88",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad83e5d3-61f7-4317-ac8c-4f46ab673b9c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4be8700b-bbe7-4833-94ed-4a0cf13714c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a177407f-1154-4158-82ff-7f252d5a3cc7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74cbec07-58fa-4afe-9e4a-7d6ddfa7495a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a10cad0-477f-45b1-9bd1-c84fa5ee0555",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca077657-c3b2-42b0-ab5c-52a84b3f87fb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2438c039-a8ba-47f4-8d46-9d163d3f408a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8263c2fc-aa77-4e00-a632-ad0def800742",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "420fc8f2-ea94-4495-935f-deb2f2a9026f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc35d271-d2ef-4244-b473-426e64e78580",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
